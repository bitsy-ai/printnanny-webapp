
// octoprint shows a "possible external address detected" warning that needs to be dismissed if domain is not in:
describe('Log into OctoPrint interface', () => {
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    beforeEach(() => {
        cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
    })
    it('Installs OctoPrint Nanny plugin', () => {
        cy.get("#navbar_show_settings").click()    
        cy.get('#settings_plugin_pluginmanager_link a').click()
        cy.contains("Get More...").click()
        cy.get('#settings_plugin_pluginmanager_repositorydialog form input').eq(1).type(Cypress.env('PRINT_NANNY_PLUGIN_ARCHIVE'))

        cy.get('#settings_plugin_pluginmanager_repositorydialog form .btn.btn-primary').first().click({force: true})
        cy.contains('A restart is needed for the changes to take effect.', {timeout: 60000})
        
        cy.contains('Restart now', {timeout: 60000}).click()
        cy.contains('Proceed', {timeout: 60000}).click()
        cy.contains('Reload now', {timeout: 60000}).click()
        cy.get('#tab_plugin_octoprint_nanny')
    })

    it('Runs Print Nanny setup wizard (OctoPrint)', () => {
        if (Cypress.$('#plugin_octoprint_nanny_wizard').length > 0){
            cy.visit(OCTOPRINT_URL)
            cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
            cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_settings_auth_token_basic').clear().type(PRINT_NANNY_TOKEN)
            cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_test_auth_token').click()
                .get('#octoprint_nanny_alert_auth').should('have.class', 'alert-success')
            cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_device_registration').click()
            cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_alert_device_registration').should('have.class', 'alert-success')
            cy.get('button[name=finish]').click()
            cy.get('#tab_plugin_octoprint_nanny').click()
        }
    })
})