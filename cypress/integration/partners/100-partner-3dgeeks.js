import { PartnersGeeks3dApiFactory, Configuration } from '../../../clients/typescript'

require('../../../clients/typescript')
// import { Configuration } from 'print-nanny-client/configuration'

describe('3D Geeks Integration Tests', () => {
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const DJANGO_SUPERUSER_PASSWORD = Cypress.env('DJANGO_SUPERUSER_PASSWORD')
    // axios api client expects base url without trailing slash
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL').substr(0, Cypress.env('PRINT_NANNY_URL').length-1)


    beforeEach(() => {
        cy.printNannyLogin(PRINT_NANNY_EMAIL, DJANGO_SUPERUSER_PASSWORD)
        cy.manageDevice()
      })

    it('Marks 3D Geeks token as verfied, sends test alert push', () => {

        cy.view3DGeeksToken().then(token =>{
            const apiConfig = new Configuration({
                basePath: PRINT_NANNY_URL,
                accessToken: token,

            })

            const geeks3DApi = PartnersGeeks3dApiFactory(apiConfig, PRINT_NANNY_URL)
            return geeks3DApi.metadataRetrieve(token).then(res =>{
                expect(res.data.verified).to.be.true
                return cy.get('#octoprint-device-partner-3dgeeks-modal button.close').click()
                    .reload()
                    .get('button').contains('Revoke 3D Geeks Access')
                    .get('button').contains('Test Alert').click()
            })
        })
    })

    it('Revokes Device 3D Geeks token', () => {
        cy.get3DGeeksToken().then(token1 =>{
            return cy.revoke3DGeeksToken()
                .get3DGeeksToken(token2 => expect(token1).not.to.equal(token2))
                .get('button').contains('Connect 3D Geeks')
        })
        
    })

})