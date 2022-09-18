// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from 'uuid';

describe.only("Shop and Checkout (SDWire)", () => {

  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutSessionUrl = ""
  let checkoutRedirectUrl = ""
  const password = "cypress1234";
  it("Shop should redirect to Stripe CheckoutSession (anonymous checkout)", () => {
    cy.visit("/shop/sdwire");

    // customer should be prompted to enter email
    cy.contains("Enter your email address or");
    cy.get("input#email").click().type(email).get("button[type=submit]").click().then(() => {
      // set checkoutSessionUrl / checkoutRedirectUrl for use in subsequent tests
      return cy.url({ timeout: 60000 }).should("contain", "checkout.stripe.com").then(url => {
        checkoutSessionUrl = url
        const segments = url.split('/');
        checkoutRedirectUrl = `/shop/thank-you/${segments.pop()}`
      })
    });
  });

  it("Stripe CheckoutSession should redirects back to shop on success (anonymous checkout)", () => {
    const sentArgs = { email, url: checkoutSessionUrl, checkoutRedirectUrl };
    // cy.origin allows use to make cross-origin requests, with limitations
    cy.origin("https://checkout.stripe.com", { args: sentArgs }, ({ email, url, checkoutRedirectUrl }) => {
      cy.visit(url);
      const shippingName = "Bitsy AI Labs";
      const address1 = "747 Howard St";
      const city = "San Francisco"
      const zip = "94107"
      const state = "California"

      const cardNumber = "4242 4242 4242 4242"
      const exp = "05/25"
      const cvc = "123"

      cy.get("input[name=shippingName]").type(shippingName);
      cy.get("input[name=shippingAddressLine1]").type(address1).type('{enter}');
      cy.get("input[name=shippingLocality]").type(city);
      cy.get("input[name=shippingPostalCode]").type(zip);
      // cy.get("input[name=shippingAdministrativeArea]").click().contains(state).click();

      cy.get("input[name=cardNumber]").type(cardNumber);
      cy.get("input[name=cardExpiry]").type(exp);
      cy.get("input[name=cardCvc]").type(cvc);
      cy.get("input[name=cardUseShippingAsBilling]").check().then(() => {
        cy.get("button[type=submit]").contains("Pay").click().wait(10000);
      });
    });
  });

  it("Stripe CheckoutSession redirect should finish account registration (anonymous checkout)", () => {
    cy.visit(checkoutRedirectUrl);
    cy.contains("Finish Account Registration");
    cy.get("input[name=email]").type(email);

    cy.get("input[name=password]").type(password);
    cy.get("input[name=passwordConfirmation]").type(password);

    cy.get("button[type=submit]").click();

    cy.contains(`Success! Created account for ${email}`);

  });

})