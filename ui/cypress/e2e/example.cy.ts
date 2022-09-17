// https://docs.cypress.io/api/introduction/api.html

describe("Landing Page", () => {
  it("Rejects invalid email", () => {
    cy.visit("/");
    let invalid = "foo123"
    cy.get("input#email").click().type(invalid).get("button#email-submit").click();
    cy.contains(`${invalid} must be a valid email`);
  });
});
