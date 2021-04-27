
describe('3D Geeks Setup', () => {
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    before(() => {
        cy.printNannyLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD) 
    
      })

    it('Shows 3D geeks token as QR code', () => {
        if (Cypress.$('#dashboard-octoprint-devices tr').length > 0){
            cy.get('#dashboard-octoprint-devices tr').last().contains('Manage Device').click()
            cy.get('button').contains('Connect 3D Geeks').click()
        }
    })

})