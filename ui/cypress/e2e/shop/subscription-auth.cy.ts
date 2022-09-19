// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from "uuid";

describe("Shop and Checkout (SDWire, Authenticated)", () => {
  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutSessionUrl = "";
  let checkoutRedirectUrl = "";
  const validPassword = "cypress1234";

  const billingName = "Bitsy AI Labs";
  const address1 = "747 Howard St";
  const city = "San Francisco";
  const zip = "94107";

  const cardNumber = "4242 4242 4242 4242";
  const exp = "05/25";
  const cvc = "123";

  before(() => {
    cy.registerUser(email, validPassword).then(() => {
      return cy.loginUser(email, validPassword);
    });
  });

  it("Shop should redirect to Stripe CheckoutSession (authenticated checkout)", () => {
    cy.visit("/shop/founding-membership");
    // should show Dashboard / Logout buttons
    cy.contains("Dashboard");
    cy.contains("Logout");

    cy.contains("Checkout with Stripe")
      .click()
      .then(() => {
        // set checkoutSessionUrl / checkoutRedirectUrl for use in subsequent tests
        return cy
          .url({ timeout: 60000 })
          .should("contain", "checkout.stripe.com")
          .then((url) => {
            checkoutSessionUrl = url;
            const segments = url.split("/");
            checkoutRedirectUrl = `/shop/thank-you/${segments.pop()}`;
          });
      });
  });

  it("Stripe CheckoutSession should redirects back to shop on success (authenticated checkout)", () => {
    const sentArgs = {
      email,
      url: checkoutSessionUrl,
      checkoutRedirectUrl,
      billingName,
      address1,
      city,
      zip,
      cardNumber,
      cvc,
      exp,
    };
    // cy.origin allows use to make cross-origin requests, with limitations
    cy.origin(
      "https://checkout.stripe.com",
      { args: sentArgs },
      ({ url, billingName, address1, city, zip, cardNumber, cvc, exp }) => {
        cy.visit(url);
        cy.get("input[name=cardNumber]").type(cardNumber);
        cy.get("input[name=cardExpiry]").type(exp);
        cy.get("input[name=cardCvc]").type(cvc);
        cy.get("input[name=billingName]").type(billingName)
        cy.get("input[name=billingAddressLine1]")
          .type(address1)
          .type("{enter}");
        cy.get("input[name=billingLocality]").type(city);
        cy.get("input[name=billingPostalCode]").type(zip);
        cy.get("button[type=submit]", { timeout: 60000 }).should('have.class', 'SubmitButton--complete').click().contains("Processing");

      }
    );

    cy.url({ timeout: 60000 }).should("contain", "/shop/thank-you/");
  });

  it("Stripe CheckoutSession redirect should show confirmation (authenticated checkout)", () => {
    cy.visit(checkoutRedirectUrl);

    // confirmation page should show shipping address
    cy.contains(billingName);
    cy.contains(address1);
    cy.contains(city);
    cy.contains(zip);

    // subscription confirm screen should show open dashboard button after account registration
    cy.get("button").contains("Open Dashboard")

  });
});
