
// octoprint shows a "possible external address detected" warning that needs to be dismissed if domain is not in:
const local_addresses = ['127.0.0.1', 'localhost']
describe('Log into OctoPrint interface', () => {

    beforeEach(() => {
        const octoprint_url = Cypress.env('OCTOPRINT_URL')
        cy.visit(octoprint_url, {timeout: 600000}) // sandbox: wait for octoprint deployment to be available
        cy.get("#login-user").type(Cypress.env('PRINT_NANNY_EMAIL'))
        cy.get("#login-password").type(Cypress.env('PRINT_NANNY_PASSWORD'))
        cy.get("#login-button").click()
        
        if (local_addresses.includes(window.location.hostname)){
            console.log("Cypress is running against local instance")
        } else {
            console.log("Cypress is running against remote sandbox")
            cy.get("button").contains("Ignore").click()
        }

    })
    it('Installs OctoPrint Nanny plugin', () => {
        cy.get("#navbar_show_settings").click()    
        cy.get('#settings_plugin_pluginmanager_link a').click()
        cy.contains("Get More...").click()
        cy.get('#settings_plugin_pluginmanager_repositorydialog form input').eq(1).type(Cypress.env('PRINT_NANNY_PLUGIN_ARCHIVE'))

        cy.get('#settings_plugin_pluginmanager_repositorydialog form .btn.btn-primary').first().click({force: true})
        cy.contains('A restart is needed for the changes to take effect.', {timeout: 60000})
        
        cy.contains('Restart now', {timeout: 60000}).click()
        cy.contains('Proceed').click()
        cy.get('#tab_plugin_octoprint_nanny')
    })
})