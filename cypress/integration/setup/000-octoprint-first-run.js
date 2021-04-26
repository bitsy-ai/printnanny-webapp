import { onlyOn, skipOn } from '@cypress/skip-test'

describe('OctoPrint initial setup', () => {
  const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
  const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
  const PRINT_NANNY_TOKEN = Cypress.env('PRINT_NANNY_TOKEN')
  before(() => {
    cy.visit(Cypress.env('OCTOPRINT_URL'), {timeout: 600000}) // sandbox: wait for octoprint deployment to be available

  })

  it('Complete setup wizard or pass if already completed', () => {
    if (Cypress.$('#wizard_dialog').length > 0){
      cy.get('#wizard_dialog')  
      cy.get('button[name=next]').click()
      cy.get('button[name=next]').click()
      cy.get('#wizard_plugin_corewizard_acl input')
        .each((el, index, list) =>{
          if (index == 0){
            cy.wrap(el).type(Cypress.env('PRINT_NANNY_EMAIL'))
          } else {
            cy.wrap(el).type(Cypress.env('PRINT_NANNY_PASSWORD'))
          }
        })
  
      cy.get('#wizard_plugin_corewizard_acl .controls a').contains('Create Account').click({force: true})
      cy.get('button[name=next]').click()
      cy.contains("Disable Anonymous Usage Tracking").click()
      cy.wait(1600)
      cy.get('button[name=next]').click()
      cy.contains("Disable Connectivity Check").click()
      cy.wait(1600)
      cy.get('button[name=next]').click()
      cy.contains("Disable Plugin Blacklist Processing").click()
      cy.wait(1600)
      cy.get('button[name=next]').click()
      cy.get('button[name=next]').click()
      cy.get('button[name=next]').click()
      cy.get('button[name=finish]').click()
    } else {
      console.log("Skipping OctoPrint initial setup wizard (already done)")
    }

  })

  it('Installs OctoPrint Nanny plugin', () => {
    cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
    cy.get("#navbar_show_settings").click()    
    cy.get('#settings_plugin_pluginmanager_link a').click()
    cy.contains("Get More...").click()
    cy.get('#settings_plugin_pluginmanager_repositorydialog form input').eq(1).type(Cypress.env('PRINT_NANNY_PLUGIN_ARCHIVE'))

    cy.get('#settings_plugin_pluginmanager_repositorydialog form .btn.btn-primary').first().click({force: true})
    cy.contains('A restart is needed for the changes to take effect.', {timeout: 60000})

    cy.contains('Restart now', {timeout: 60000}).click().then(() =>{
      
      const update_available = Cypress.$('.ui-pnotify[aria-live=assertive] h4').text() == 'Update Available'
      if (update_available){
        console.log('Dismissing notification')
        cy.get('.ui-pnotify[aria-live=assertive]').find('button').contains('Ignore').click()
  
      }
      return cy.get('.modal-footer .btn').contains('Proceed').click()
        .get('#reloadui_overlay button').contains('Reload now').click({timeout: 60000})
    })
        

  })
  
  it('Runs Print Nanny setup wizard (OctoPrint)', () => {
      cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD).then( ()=>{
        if (Cypress.$('#octoprint_nanny_wizard_basic').length > 0){
          cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_settings_auth_token_basic').clear().type(PRINT_NANNY_TOKEN)
          cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_test_auth_token').click()
              .get('#octoprint_nanny_alert_auth').should('have.class', 'alert-success')
          cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_device_registration').click()
          cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_alert_device_registration').should('have.class', 'alert-success')
          cy.get('button[name=finish]').click()
        }
      })
  })
})