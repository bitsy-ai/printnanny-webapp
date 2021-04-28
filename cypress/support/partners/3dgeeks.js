

Cypress.Commands.add('view3DGeeksToken', () => {
    return cy.get('button').contains('Connect 3D Geeks').click()
        .get('#partners-3dgeeks-token').then($token => {
            return new Cypress.Promise((resolve, reject) => {
                resolve($token[0].innerText)
            })
        })
})

Cypress.Commands.add('get3DGeeksToken', () => {
    return Cypress.$('#partners-3dgeeks-token').innerText
})

Cypress.Commands.add('revoke3DGeeksToken', () => {
   return cy.get('button').contains('Revoke 3D Geeks Access').click()
    
})