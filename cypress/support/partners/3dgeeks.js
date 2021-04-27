Cypress.Commands.add('get3DGeeksToken', () => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_API_URL')
    if (Cypress.$('#dashboard-octoprint-devices tr').length > 0){
        cy.get('#dashboard-octoprint-devices tr').last().contains('Manage Device').click()
        cy.get('button').contains('Connect 3D Geeks').click()
        cy.get('#partners-3dgeeks-token').then($token => {
            return new Cypress.Promise((resolve, reject) => {
                resolve($token[0].innerText)
            })
        })
    } 
})