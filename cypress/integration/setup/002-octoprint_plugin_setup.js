
describe('Print Nanny setup wizard', () => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    const PRINT_NANNY_TOKEN = Cypress.env('PRINT_NANNY_TOKEN')
    const OCTOPRINT_URL = Cypress.env('OCTOPRINT_URL')




    it('Retrieves Print Nanny auth token', () => {
        cy.fetchPrintNannyToken(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD).then($token => assert.exists($token))
    })

    it('Retrieves device info from dashboard', () =>{
        cy.printNannyLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
        cy.get('#dashboard-octoprint-devices tr').should('have.length', 2)
        cy.get('#dashboard-octoprint-devices tr').last().contains('View Metadata').click()
        cy.get('#octoprint-device-metadata-modal-1').contains('Metadata')
    })
})