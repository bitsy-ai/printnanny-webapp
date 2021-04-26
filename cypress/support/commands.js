// ***********************************************
// This example commands.js shows you how to
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

Cypress.Commands.add('octoprintLogin', (email, password) => {
    const url = Cypress.env('OCTOPRINT_URL')
    cy.visit(url, {timeout: 600000}) // sandbox: wait for octoprint deployment to be available
    cy.get("#login-user").type(email)
    cy.get("#login-password").type(password)
    cy.get("#login-button").click()
    
    if (local_addresses.includes(window.location.hostname)){
        console.log("Cypress is running against local instance")
    } else {
        console.log("Cypress is running against remote sandbox")
        cy.get("button").contains("Ignore").click()
    }  
})


Cypress.Commands.add('printNannyyLogin', (email, password) => {
    const _url = Cypress.env('PRINT_NANNY_URL')
    cy.visit(url, {timeout: 600000}) // sandbox: wait for octoprint deployment to be available
    cy.get("#login-user").type(email)
    cy.get("#login-password").type(password)
    cy.get("#login-button").click()
    
    if (local_addresses.includes(window.location.hostname)){
        console.log("Cypress is running against local instance")
    } else {
        console.log("Cypress is running against remote sandbox")
        cy.get("button").contains("Ignore").click()
    }  
})

Cypress.Commands.add('fetchPrintNannyToken', (email, password) => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_LOGIN_URL = new URL('/accounts/login', PRINT_NANNY_URL).href
    cy.visit(PRINT_NANNY_LOGIN_URL)
    // hide django debug toolbar
    cy.get('#djHideToolBarButton').click()
    cy.get('input[name=login]').type(email)
    cy.get('input[name=password]').type(password)
    cy.get('button[type=submit]').click()
    cy.get('#show-token').click()
    return cy.get('#token').then($input => $input.val)
})