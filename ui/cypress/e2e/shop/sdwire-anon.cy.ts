import { v4 as uuidv4 } from "uuid";

describe("Shop and Checkout (SDWire, Anonymous)", () => {
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

  it("Shop should redirect to Stripe CheckoutSession (anonymous checkout)", () => {
    cy.visit("/shop/sdwire");

    // customer should be prompted to enter email
    cy.contains("Enter your email address or");
    cy.get("input#email")
      .click()
      .type(email)
      .get("button[type=submit]")
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

  it("Stripe CheckoutSession should redirect back to shop on success (anonymous checkout)", () => {
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
    };
    // cy.origin allows use to make cross-origin requests, with limitations
    cy.origin(
      "https://checkout.stripe.com",
      { args: sentArgs },
      ({ url, shippingName, address1, city, zip, cardNumber, cvc, exp }) => {
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
        cy.get("input[name=cardUseShippingAsBilling]")
          .check();
        cy.get("button[type=submit]").contains("Pay").should('have.class', 'SubmitButton--complete').click().contains("Processing");
      }
    );

    cy.url({ timeout: 60000 }).should("contain", "/shop/thank-you/");
  });

  it("Stripe CheckoutSession redirect should finish account registration (anonymous checkout)", () => {
    cy.visit(checkoutRedirectUrl);

    // account registration should succeed
    cy.contains("Finish Account Registration");
    cy.get("input[name=password]").clear().type(validPassword);
    cy.get("input[name=passwordConfirmation]").clear().type(validPassword);
    cy.get("button[type=submit]").click();
    cy.contains(`Success! Created account for ${email}`);

    // confirmation page should show shipping address
    cy.contains(shippingName);
    cy.contains(address1);
    cy.contains(city);
    cy.contains(zip);

    // a shipping method should be present for physical goods
    cy.contains("Shipping method");
  });
});