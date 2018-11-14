<template>
  <section class="container mt-5">
    <b-jumbotron
      class="py-3"
      bg-variant="white"
      text-variant="dark"
      border-variant="danger">
      <template slot="header">
        <span class="display-4">Cura Network Bounty</span>
      </template>
      <template slot="lead">
        Earn generous stakes by carrying out the tasks you love to do. 
        Let’s get as many people as possible familiar with the Cura Network project, 
        let them know what’s offered and how this revolution will benefit them.
      </template>
      <b-btn 
        v-b-modal.auth
        v-if="!$auth.loggedIn"
        variant="primary"
        size="lg"
        class="mt-3"
        href="#">Start participating</b-btn>
      <hr class="my-4">
      <p class="small">
        <b-link href="#">Terms & Conditions</b-link> · 
        <b-link 
          href="https://curanetwork.co/whitepaper/" 
          target="_blank">Whitepaper
        </b-link> · 
        <b-link 
          href="https://www.youtube.com/watch?v=hEpMtp4gFfU" 
          target="_blank">Explainer Video
        </b-link> · 
        <b-link 
          href="https://t.me/CuraNetworkPlatform" 
          target="_blank"> Telegram
        </b-link> ·  
        <b-link 
          href="https://github.com/curanetwork" 
          target="_blank">Github
        </b-link> · 
        <b-link 
          href="https://web.facebook.com/curanetwork" 
          target="_blank">Facebook
        </b-link> · 
        <b-link 
          href="https://twitter.com/CuraNetwork" 
          target="_blank">Twitter
        </b-link> · 
        <b-link 
          href="https://www.youtube.com/channel/UCr4xUHghM8p8fT2oa3Co2Sw" 
          target="_blank">Youtube
        </b-link> · 
        <b-link 
          href="https://medium.com/@curanetwork" 
          target="_blank">Medium
        </b-link> · 
        <b-link 
          href="#" 
          target="_blank">Linkedin
        </b-link> · 
        <b-link 
          href="https://www.instagram.com/curanetwork" 
          target="_blank">Instagram
        </b-link> · 
        <b-link 
          href="#" 
          target="_blank">Bitcointalk
        </b-link> · 
        <b-link 
          href="https://www.reddit.com/user/curanetwork" 
          target="_blank">Reddit
        </b-link>
      </p>
    </b-jumbotron>
    <b-card no-body>
      <b-tabs 
        pills 
        card 
        vertical>
        <b-tab
          title="Bounties"
          active>
          <div>
            <b-card-group 
              deck
              class="mb-3">
              <b-card
                text-variant="dark"
                header="Facebook"
                header-bg-variant="primary"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Like, share, and post about Cura Network on Facebook.</p>
                <b-button 
                  href="#"
                  variant="outline-primary">Details</b-button>
              </b-card>
              <b-card
                text-variant="dark"
                header="Bitcointalk Signature"
                header-bg-variant="secondary"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-secondary">Details</b-button>
              </b-card>
              <b-card 
                text-variant="dark"
                header="Article/Content"
                header-bg-variant="success"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-success">Details</b-button>
              </b-card>
            </b-card-group>
            <b-card-group 
              deck
              class="mb-3">
              <b-card 
                text-variant="dark"
                header="Twitter"
                header-bg-variant="info"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-info">Details</b-button>
              </b-card>
              <b-card
                text-variant="dark"
                header="Translation"
                header-bg-variant="warning"
                header-text-variant="dark"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-warning">Details</b-button>
              </b-card>
              <b-card
                text-variant="dark"
                header="Youtube"
                header-bg-variant="danger"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-danger">Details</b-button>
              </b-card>
            </b-card-group>
            <b-card-group 
              deck
              class="mb-3">
              <b-card 
                text-variant="dark"
                header="Reddit"
                header-bg-variant="dark"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-dark">Details</b-button>
              </b-card>
              <b-card 
                text-variant="dark"
                header="Instagram"
                header-bg-variant="dark"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-dark">Details</b-button>
              </b-card>
              <b-card
                text-variant="dark"
                header="Telegram"
                header-bg-variant="primary"
                header-text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <b-button 
                  href="#"
                  variant="outline-primary">Details</b-button>
              </b-card>
            </b-card-group>
          </div>
        </b-tab>
        <b-tab 
          title="Weekly leaderboard" >
          <b-table 
            :items="items" 
            :fields="fields" 
            striped 
            hover/>
        </b-tab>
        <b-tab title="Hall of fame">
          <b-table 
            :items="items" 
            :fields="fields" 
            striped 
            hover/>
        </b-tab>
      </b-tabs>
    </b-card>
    <!-- Modal Component -->
    <b-modal 
      id="auth" 
      :title="auth.title" 
      :ok-title="auth.action"
      :ok-disabled="errors.any() || !isFilled(auth.form)"
      centered
      ok-variant="danger"
      ok-only
      @ok="handleAuthForm">
      <b-form 
        v-if="auth.form === 'login'" 
        data-vv-scope="login">
        <notif 
          :type="notif[0]" 
          :message="notif[1]" 
          @clear="notif = ['', '']"/>
        <b-form-group>
          <b-form-input 
            v-validate="'required'" 
            id="username"
            :state="errors.has('login.username') ? !errors.has('login.username') : null"
            v-model="auth.data.username"
            name="username"
            aria-describedby="username-feedback"
            type="text"
            placeholder="Enter username"/>
          <b-form-invalid-feedback id="username-feedback">
            {{ errors.first('login.username') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group>
          <b-form-input 
            v-validate="'required'" 
            id="password"
            :state="errors.has('login.password') ? !errors.has('login.password') : null"
            v-model="auth.data.password"
            name="password"
            aria-describedby="password-feedback"
            type="password"
            placeholder="**********"/>
          <b-form-invalid-feedback id="password-feedback">
            {{ errors.first('login.password') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-link 
          class="text-danger" 
          @click="modal('forgot')"><small>Forgot your password?</small></b-link> | 
        <b-link 
          class="text-danger" 
          @click="modal('signup')"><small>Create an account</small></b-link>
      </b-form>
      <b-form 
        v-if="auth.form === 'forgot'" 
        data-vv-scope="forgot">
        <b-form-group>
          <b-form-input
            v-validate="'required|email'" 
            id="email"
            :state="errors.has('forgot.email') ? !errors.has('forgot.email') : null"
            v-model="auth.data.email"
            name="email"
            aria-describedby="email-feedback"
            type="email"
            placeholder="Enter your email address"/>
          <b-form-invalid-feedback id="email-feedback">
            {{ errors.first('forgot.email') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-link 
          class="text-danger" 
          @click="modal('login')"><small>I already have an account</small></b-link>
      </b-form>
      <b-form 
        v-if="auth.form === 'signup'" 
        data-vv-scope="signup">
        <p>
          <b-link
            href="https://t.me/CuraNetworkBounty"
            target="_blank"
          >Click here</b-link> to join the bounty Telegram group
        </p>
        <b-form-group>
          <b-form-input 
            v-validate="'required'" 
            id="username"
            :state="errors.has('signup.telegram username') ? !errors.has('signup.telegram username') : null"
            v-model="auth.data.username"
            name="telegram username"
            aria-describedby="username-feedback"
            type="text"
            placeholder="Enter Telegram username"/>
          <b-form-invalid-feedback id="username-feedback">
            {{ errors.first('signup.telegram username') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group>
          <b-form-input
            v-validate="'required|email'" 
            id="email"
            :state="errors.has('signup.email') ? !errors.has('signup.email') : null"
            v-model="auth.data.email"
            name="email"
            aria-describedby="email-feedback"
            type="email"
            placeholder="Enter email address"/>
          <b-form-invalid-feedback id="email-feedback">
            {{ errors.first('signup.email') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          description="CAUTION: This cannot be changed. All tokens will be sent to this address during token distribution">
          <b-form-input 
            v-validate="'required'" 
            id="eth-address"
            :state="errors.has('signup.ethereum address') ? !errors.has('signup.ethereum address') : null"
            v-model="auth.data.ethAddress"
            name="ethereum address"
            type="text"
            aria-describedby="eth-address-feedback"
            placeholder="Enter Ethereum Address"/>
          <b-form-invalid-feedback id="eth-address-feedback">
            {{ errors.first('signup.ethereum address') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          description="Password">
          <b-form-input 
            v-validate="'required'" 
            id="password"
            ref="re_password"
            :state="errors.has('signup.password') ? !errors.has('signup.password') : null"
            v-model="auth.data.password"
            name="password"
            aria-describedby="password-feedback"
            type="password"
            placeholder="**********"/>
          <b-form-invalid-feedback id="password-feedback">
            {{ errors.first('signup.password') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          description="Retype password">
          <b-form-input 
            v-validate="'required|confirmed:re_password'" 
            id="re-password"
            :state="errors.has('signup.retype password') ? !errors.has('signup.retype password') : null"
            name="retype password"
            aria-describedby="re-password-feedback"
            type="password"
            placeholder="**********"/>
          <b-form-invalid-feedback id="re-password-feedback">
            {{ errors.first('signup.retype password') }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-link 
          class="text-danger" 
          @click="modal('login')"><small>I already have an account</small></b-link>
      </b-form>
    </b-modal>
  </section>
</template>

<script>
import Notif from '~/components/Notif'

export default {
  components: {
    Notif
  },

  data: () => ({
    notif: [],
    auth: {
      form: 'login',
      title: 'Log in',
      action: 'Log in',
      data: {
        username: '',
        email: '',
        ethAddress: '',
        password: ''
      }
    },
    fields: ['first_name', 'last_name', 'age'],
    items: [
      {
        isActive: true,
        age: 40,
        first_name: 'Dickerson',
        last_name: 'Macdonald'
      },
      { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
      { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
      { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
    ]
  }),

  async asyncData({ app }) {
    try {
      let response = await app.$axios.$get('/bounties')
      return {
        bounties: response.data
      }
    } catch (e) {}
  },

  methods: {
    modal(form) {
      switch (form) {
        case 'login':
          this.auth.form = form
          this.auth.title = 'Log in'
          this.auth.action = 'Log in'
          break
        case 'signup':
          this.auth.form = form
          this.auth.title = 'Create an account'
          this.auth.action = 'Submit'
          break
        case 'forgot':
          this.auth.form = form
          this.auth.title = 'Reset password'
          this.auth.action = 'Send me password reset link'
          break
      }
      this.auth.data = {
        username: '',
        email: '',
        ethAddress: '',
        password: ''
      }
      this.errors.clear()
    },

    isFilled(form) {
      switch (form) {
        case 'login':
          return this.auth.data.username && this.auth.data.password
          break
        case 'signup':
          return (
            this.auth.data.username &&
            this.auth.data.email &&
            this.auth.data.ethAddress &&
            this.auth.data.password
          )
          break
        case 'forgot':
          return this.auth.data.email
          break
      }
    },

    async login() {
      try {
        await this.$auth.loginWith('local', {
          data: {
            username: this.auth.data.username,
            password: this.auth.data.password
          }
        })
        this.notif = ['', '']
        this.$router.replace({ name: 'in' })
      } catch (e) {
        this.notif = ['danger', e.response.data['non_field_errors']]
      }
    },

    async signup() {
      try {
        await this.$axios.$post('/auth/users/create', {
          username: this.auth.data.username,
          email: this.auth.data.email,
          ethAddress: this.auth.data.ethAddress,
          password: this.auth.data.password
        })
        this.notif = ['', '']
        this.login()
      } catch (e) {
        this.notif = ['danger', e.response.data['non_field_errors']]
      }
    },

    handleAuthForm(evt) {
      evt.preventDefault()
      switch (this.auth.form) {
        case 'login':
          this.login()
          break
        case 'signup':
          this.signup()
          break
        case 'forgot':
          break
      }
    }
  }
}
</script>

<style>
</style>
