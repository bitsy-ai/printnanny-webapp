
describe('Log into OctoPrint interface', () => {

    before(() => {
        cy.visit(Cypress.env('OCTOPRINT_URL'), {timeout: 600000}) // sandbox: wait for octoprint deployment to be available
        cy.get("#login-user").type(Cypress.env('PRINT_NANNY_EMAIL'))
        cy.get("#login-password").type(Cypress.env('PRINT_NANNY_PASSWORD'))
        cy.get("#login-button").click()
        cy.get(".ui-pnotify button").contains("Ignore").click()
    })
    it('Install OctoPrint Nanny plugin', () => {
        cy.get("#navbar_show_settings").click()    
        cy.get('#settings_plugin_pluginmanager_link a').click()
        cy.contains("Get More...").click()
        cy.get('#settings_plugin_pluginmanager_repositorydialog form input').eq(1).type(Cypress.env('PRINT_NANNY_PLUGIN_ARCHIVE'))

        cy.get('#settings_plugin_pluginmanager_repositorydialog form .btn.btn-primary').first().click({force: true})
        cy.contains('A restart is needed for the changes to take effect.', {timeout: 60000})

        cy.contains('Restart now', {timeout: 60000}).click()
        cy.contains('Proceed', {timeout: 60000}).click()
        cy.contains('Reload now', {timeout: 60000}).click()
        cy.contains("#wizard_plugin_octoprint_nanny")
    })
})