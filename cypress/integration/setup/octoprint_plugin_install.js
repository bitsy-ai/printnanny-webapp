
describe('Log into OctoPrint interface', () => {

    before(() => {
        cy.visit(Cypress.env('OCTOPRINT_URL'))
        cy.get("#login-user").type(Cypress.env('OCTOPRINT_USERPASS'))
        cy.get("#login-password").type(Cypress.env('OCTOPRINT_USERPASS'))
        cy.get("#login-button").click()
    })
    it('Install OctoPrint Nanny plugin', () => {
        cy.get("#navbar_show_settings").click()    
        cy.get('#settings_plugin_pluginmanager_link a').click()
        cy.contains("Get More...").click()
        cy.get('#settings_plugin_pluginmanager_repositorydialog form input').eq(1).type(Cypress.env('PRINT_NANNY_PLUGIN_ARCHIVE'))

        cy.get('#settings_plugin_pluginmanager_repositorydialog form .btn.btn-primary').first().click({force: true})
        cy.contains('A restart is needed for the changes to take effect.', {timeout: 20000})

        cy.contains('Restart now', {timeout: 20000}).click()
        cy.contains('Proceed', {timeout: 20000}).click()
        cy.contains('Reload now', {timeout: 20000}).click()
        cy.contains("#wizard_plugin_octoprint_nanny")
    })
})