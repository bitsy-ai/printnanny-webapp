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

const fs = require('fs') 

require('./partners/3dgeeks')

Cypress.Commands.add('octoprintLogin', (email, password) => {
    const local_addresses = ['127.0.0.1', 'localhost']
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


Cypress.Commands.add('printNannyLogin', (email, password) => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_LOGIN_URL = new URL('/accounts/login', PRINT_NANNY_URL).href
    cy.visit(PRINT_NANNY_LOGIN_URL)
    // hide django debug toolbar
    cy.get('#djHideToolBarButton').click()
    cy.get('input[name=login]').type(email)
    cy.get('input[name=password]').type(password)
    cy.get('button[type=submit]').click()
})

Cypress.Commands.add('getPrintNannyToken', (email, password) => {
    cy.printNannyLogin(email, password)
    cy.get('#show-token').click()
    return cy.get('#token').then($input => {
        return $input.val
    })
})

Cypress.Commands.add('manageDevice', (octoprint_device_id=null) =>{
    if (octoprint_device_id == null){
        if (Cypress.$('#dashboard-octoprint-devices tr').length > 0){
            return cy.get('#dashboard-octoprint-devices tr').last().contains('Manage Device').click()
        }
    }
})