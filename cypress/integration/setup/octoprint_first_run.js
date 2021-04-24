describe('OctoPrint initial setup wizard', () => {
      it('Create a new user or log in with existing user', () => {
        cy.visit(Cypress.env('OCTOPRINT_URL'))
        cy.contains('Setup Wizard')
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

        
      })
  })