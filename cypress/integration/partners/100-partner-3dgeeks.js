import { Geeks3dApiFactory, Configuration } from '../../../clients/typescript'

require('../../../clients/typescript')
// import { Configuration } from 'print-nanny-client/configuration'

describe('3D Geeks Setup', () => {
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    const PRINT_NANNY_API_URL = Cypress.env('PRINT_NANNY_API_URL')


    before(() => {
        cy.printNannyLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
      })

    it('Marks 3D token as verfied after authorized request', () => {
        cy.get3DGeeksToken().then($token =>{
            const token = $token.innerText
            const apiConfig = new Configuration({
                basePath: process.env.BASE_API_URL,
                baseOptions: {
                  accessToken: token,
                  withCredentials: true
                }
            })

            geeks3DApi = Geeks3dApiFactory(apiConfig)
            return geeks3DApi.metadataRetrieve(token)
        })

    })

    it('Sends alert to 3D Geeks push endpoint', () => {
        
    })

})