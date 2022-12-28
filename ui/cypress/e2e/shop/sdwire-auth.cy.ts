// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from "uuid";

describe("Shop and Checkout (SDWire, Authenticated)", () => {
  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutSessionUrl = "";
  let checkoutRedirectUrl = "";
  const validPassword = "cypress1234";

  const shippingName = "Bitsy AI Labs";
  const address1 = "747 Howard St";
  const city = "San Francisco";
  const zip = "94107";

  const cardNumber = "4242 4242 4242 4242";
  const exp = "05/25";
  const cvc = "123";
  const phoneNumber = "8888675309";

  before(() => {
    cy.registerUser(email, validPassword).then(() => {
      return cy.loginUser(email, validPassword);
    });
  });

  it("Shop should redirect to Stripe CheckoutSession (authenticated checkout)", () => {
    cy.visit("/shop/sdwire");
    // should show Dashboard / Logout buttons
    cy.contains("Dashboard");
    cy.contains("Logout");

    cy.contains("Pre-order with Stripe")
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
      shippingName,
      address1,
      city,
      zip,
      cardNumber,
      cvc,
      exp,
      phoneNumber
    };
    // cy.origin allows use to make cross-origin requests, with limitations
    cy.origin(
      "https://checkout.stripe.com",
      { args: sentArgs },
      ({ url, shippingName, address1, city, zip, cardNumber, cvc, exp, phoneNumber }) => {
        cy.visit(url);
        cy.get("input[name=shippingName]").type(shippingName);
        cy.get("input[name=shippingAddressLine1]")
          .type(address1)
          .type("{enter}");
        cy.get("input[name=shippingLocality]").type(city);
        cy.get("input[name=shippingPostalCode]").type(zip);
        // cy.get("input[name=shippingAdministrativeArea]").click().contains(state).click();
        cy.get("input[name=cardNumber]").type(cardNumber);
        cy.get("input[name=cardExpiry]").type(exp);
        cy.get("input[name=cardCvc]").type(cvc);
        cy.get("input[name=cardUseShippingAsBilling]").check();
        cy.get("input[name=phoneNumber]").type(phoneNumber)

        cy.get("button[type=submit]")
          .contains("Pay")
          .should("have.class", "SubmitButton--complete")
          .click()
          .contains("Processing");
      }
    );

    cy.url({ timeout: 60000 }).should("contain", "/shop/thank-you/");
  });

  it("Stripe CheckoutSession redirect should show confirmation (authenticated checkout)", () => {
    cy.visit(checkoutRedirectUrl);

    // a shipping method should be present for physical goods
    cy.contains("Shipping method", { timeout: 10000 });
    // confirmation page should show shipping address
    cy.contains(shippingName, { timeout: 10000 });
    cy.contains(address1, { timeout: 10000 });
    cy.contains(city, { timeout: 10000 });
    cy.contains(zip, { timeout: 10000 });

    // Download/print receipt button should open pay.strime.com
    cy.get("button#receipt", { timeout: 10000 })
      .click()
      .then(() => {
        // set checkoutSessionUrl / checkoutRedirectUrl for use in subsequent tests
        return cy.url({ timeout: 60000 }).should("contain", "pay.stripe.com");
      });
  });
});
