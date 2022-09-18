// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from 'uuid';

describe("Shop", () => {
  it("SDWire shop page prompts for email if not logged in", () => {
    cy.visit("/shop/sdwire");
    cy.contains("Enter your email address or");
    cy.get("input#email");

  });
  it("Subscription shop page prompts for email if not logged in", () => {
    cy.visit("/shop/founding-membership");
    cy.contains("Enter your email address or");
    cy.get("input#email");

  });


});

describe("Shop and Checkout", () => {
  it.only("SDWire checkout succeeds for anonymous user", () => {
    cy.visit("/shop/sdwire");

    // customer should be prompted to enter email
    cy.contains("Enter your email address or");

    const email = `testing-${uuidv4()}@printnanny.ai`

    cy.get("input#email").click().type(email).get("button[type=submit]").click();

  });
})