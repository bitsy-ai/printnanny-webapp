// https://docs.cypress.io/api/introduction/api.html
import { v4 as uuidv4 } from "uuid";

describe("Landing Page", () => {
  it("Rejects invalid email", () => {
    cy.visit("/");
    const invalid = "foo123";
    cy.get("input#email")
      .click()
      .type(invalid)
      .get("button#waitlist-submit")
      .click();
    cy.contains(`email must be a valid email`);
  });
  it("Signs up for email waitlist", () => {
    cy.visit("/");
    const valid = `${uuidv4()}@test.com`;
    cy.get("input#email")
      .click()
      .type(valid)
      .get("button#waitlist-submit")
      .click();
    cy.contains("Thanks for signing up!");
  });
});
