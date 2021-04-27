
describe('Print Nanny setup wizard', () => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    const PRINT_NANNY_TOKEN = Cypress.env('PRINT_NANNY_TOKEN')

    it('Retrieves Print Nanny auth token', () => {
        cy.fetchPrintNannyToken(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD).then($token => assert.exists($token))
    })

    it('Retrieves device info from dashboard or display empty message', () =>{
        if (!Cypress.$('#dashboard-octoprint-devices tr').length){
            cy.get('.content').contains("You haven't registered any OctoPrint Devices yet.")

        } else {
            cy.get('#dashboard-octoprint-devices tr').should('have.length', 2)
            cy.get('#dashboard-octoprint-devices tr').last().contains('View Metadata').click()
              .contains('Metadata')
              .wait(4000) // wait for modal fade-in animation 
              .get("#octoprint-device-metadata-modal-1 button.close[data-dismiss='modal']").click()
        }

    })

    it('Removes device from management dashboard (if device present) ', () => {
        cy.printNannyLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
        if (Cypress.$('#dashboard-octoprint-devices tr').length > 0){
            cy.get('#dashboard-octoprint-devices tr').last().contains('Manage Device').click()
            cy.get('button').contains('Remove Device').click()
            cy.get('.content').contains("You haven't registered any OctoPrint Devices yet.")
        }

    })

    it('Device re-registration succeeds in OctoPrint', () => {
        cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
        cy.get('#navbar_show_settings').click()
            .get('#settings_plugin_octoprint_nanny_link a').click()
            .get('#octoprint_nanny_settings_reset_device').click()
        cy.contains('✅ Success! Your device was issued a new identity.')

    })

})