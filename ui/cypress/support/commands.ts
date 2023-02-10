/// <reference types="cypress" />
// ***********************************************
// This example commands.ts shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
//
// declare global {
//   namespace Cypress {
//     interface Chainable {
//       login(email: string, password: string): Chainable<void>
//       drag(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       dismiss(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       visit(originalFn: CommandOriginalFn, url: string, options: Partial<VisitOptions>): Chainable<Element>
//     }
//   }
// }
import * as api from "printnanny-api-client";

const ApiConfig = new api.Configuration({
  basePath: "http://localhost:8080",
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});

Cypress.Commands.add("registerUser", (email, password) => {
  const accountsApi = api.AccountsApiFactory(ApiConfig);
  const req = {
    email,
    password1: password,
    password2: password,
  } as api.RegisterRequest;
  return accountsApi.accountsRegistrationCreate(req);
});

Cypress.Commands.add("loginUserWithPassword", (email, password) => {
  const accountsApi = api.AccountsApiFactory(ApiConfig);
  return cy.session(email, () => {
    const req = { email, password } as api.LoginRequest;
    return accountsApi.accountsLoginCreate(req);
  });
});

Cypress.Commands.add("loginUserWithMagicLink", (email: string) => {
  return cy.visit("/login/").then(() => {
    cy.get("input[name=email]").type(email);
    cy.get("button[type=submit]").click();
    const cmd = `make ci-callback-token ARGS="--email=${email}" -C ..`;
    return cy.exec(cmd).then((result: any) => {
      // once the command has completed, the callback function is called
      if (result.code != 0) {
        // log and return if we encounter an error
        console.error("Could not execute command: ", cmd);
        console.log(result.stdout);
        console.error(result.stderr);
        return;
      }
      // log the output received from the command
      const lines = result.stdout.split("\n");
      const token = lines[lines.length - 2];
      cy.get("input[name=token]").type(token);
      cy.get("button[type=submit]").click();
    });
  });
});
