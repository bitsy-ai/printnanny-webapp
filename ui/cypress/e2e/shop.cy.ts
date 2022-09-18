// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from 'uuid';

describe.only("Shop and Checkout (SDWire)", () => {

  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutSessionUrl = ""
  let checkoutRedirectUrl = ""
  it("Shop redirects to Stripe Checkout Session (anonymous checkout)", () => {
    cy.visit("/shop/sdwire");

    // customer should be prompted to enter email
    cy.contains("Enter your email address or");
    cy.get("input#email").click().type(email).get("button[type=submit]").click().then(() => {
      return cy.url().should("contain", "checkout.stripe.com").then(url => {
        checkoutSessionUrl = url
      })
    });
  });

  it("Stripe Checkout Session redirects to shop (anonymous checkout)", () => {
    const sentArgs = { email, url: checkoutSessionUrl };
    cy.origin("https://checkout.stripe.com", { args: sentArgs }, ({ email, url }) => {
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
        cy.get("button[type=submit]").contains("Pay").click().then(() => {
          return cy.url({ timeout: 60000 }).should("contain", "/shop/thank-you/").then(url => {
            checkoutRedirectUrl = url;
          });
        });

      });
    })
  })
})