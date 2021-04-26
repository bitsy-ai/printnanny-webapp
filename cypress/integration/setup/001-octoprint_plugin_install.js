
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
})