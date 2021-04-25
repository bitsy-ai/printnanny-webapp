
describe('Print Nanny setup wizard', () => {
    var PRINT_NANNY_TOKEN = null;
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_LOGIN_URL = new URL('/accounts/login', PRINT_NANNY_URL).href
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    before(() => {
        cy.visit(PRINT_NANNY_LOGIN_URL)
        cy.get('input[name=login]').type(PRINT_NANNY_EMAIL)
        cy.get('input[name=password]').type(PRINT_NANNY_PASSWORD)
        cy.get('button[type=submit]').click()
    })

    it('Runs Print Nanny plugin setup wizard', () => {

    })
})