<template>
  <b-container>
    <UserRegistration
      :first-name.sync="registration.firstName"
      :last-name.sync="registration.lastName"
      :birth-date.sync="registration.birthDate"
      :country.sync="registration.country"
      :show="showUserRegistration"
      @next="onUserRegistrationNext"
      @back="onUserRegistrationBack"
    ></UserRegistration>
    <UserIdentification
      :dni.sync="identification.dni"
      :dni-front.sync="identification.front"
      :dni-back.sync="identification.back"
      :show="showUserIdentification"
      @next="onUserIdentificationNext"
      @back="onUserIdentificationBack"
    ></UserIdentification>
    <UserDomicile
      :street-address.sync="domicile.data.streetAddress"
      :street-number.sync="domicile.data.streetNumber"
      :city.sync="domicile.data.city"
      :floor.sync="domicile.data.floor"
      :postal-code.sync="domicile.data.postalCode"
      :country.sync="domicile.data.country"
      :domicile-proof.sync="domicile.proof"
      :show="showUserDomicile"
      @next="onUserDomicileNext"
      @back="onUserDomicileBack"
    ></UserDomicile>
    <UserFinish
      :show="showUserFinish"
      @back="onUserFinishBack"
    ></UserFinish>
  </b-container>
</template>

<script>
    import { post } from '../services/api';
    import UserRegistration from './UserRegistration'
    import UserIdentification from './UserIdentification'
    import UserDomicile from './UserDomicile'
    import UserFinish from './UserFinish'

    export default {
        components: {
            UserRegistration,
            UserIdentification,
            UserDomicile,
            UserFinish
        },
        data() {
            return {
                registration: {
                    firstName: '',
                    lastName: '',
                    birthDate: '',
                    country: '',
                },
                identification: {
                    dni: '',
                    front: null,
                    back: null,
                },
                domicile: {
                    data: {
                        streetAddress: '',
                        streetNumber: '',
                        city: '',
                        floor: '',
                        postalCode: '',
                        country: '',
                    },
                    proof: null,
                },
                showUserRegistration: true,
                showUserIdentification: false,
                showUserDomicile: false,
                showUserFinish: false,
                issue: null
            }
        },
        methods: {
            onUserRegistrationBack(event) {
                event.preventDefault()

            },
            async onUserRegistrationNext(event) {
                event.preventDefault()
                const result = await post(
                    'http://localhost:5000/user', this.registration, { headers: { 'Content-Type': 'application/json' } }
                )
                if(result.statusText === 'OK') {
                  this.issue = result.data.payload.issue
                  this.showUserRegistration = false
                  this.showUserIdentification = true
                }
            },
            onUserIdentificationBack(event) {
                event.preventDefault()
                this.showUserIdentification = false
                this.showUserRegistration = true
            },
            async onUserIdentificationNext(event) {
                event.preventDefault()
                const formData = new FormData()
                formData.append('issue', JSON.stringify(this.issue))
                formData.append('dni', this.identification.dni)
                formData.append('dniFront', this.identification.front)
                formData.append('dniBack', this.identification.back)
                const result = await post(
                    'http://localhost:5000/user/id', formData, { headers: { 'Content-Type': 'multipart/form-data' } }
                )
                if(result.statusText === 'OK') {
                  this.showUserIdentification = false
                  this.showUserDomicile = true
                }
            },
            onUserDomicileBack(event) {
                event.preventDefault()
                this.showUserDomicile = false
                this.showUserIdentification = true
            },
            async onUserDomicileNext(event) {
                event.preventDefault()
                const formData = new FormData();
                formData.append('issue', JSON.stringify(this.issue))
                formData.append('domicile', JSON.stringify(this.domicile.data))
                formData.append('domicileProof', this.domicile.proof)
                const result = await post(
                    'http://localhost:5000/domicile', formData, { headers: { 'Content-Type': 'multipart/form-data' } }
                )
                if(result.statusText === 'OK') {
                  this.showUserDomicile = false
                  this.showUserFinish = true
                }
            },
            onUserFinishBack(event) {
                event.preventDefault()
                this.showUserFinish = false
                this.showUserDomicile = true
            }
        }
    }
</script>
