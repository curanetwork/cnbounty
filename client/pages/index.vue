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
        variant="primary"
        size="lg"
        class="mt-3"
        href="#"
        @click="modal('signup')">Start participating</b-btn>
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
                <p class="card-text"><font-awesome-icon :icon="['fab', 'facebook-f']" />Like, share, and post about Cura Network on Facebook.</p>
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
      centered
      ok-variant="danger"
      ok-only
      @ok="handleAuthForm">
      <b-form>
        <div v-if="auth.form === 'login'">
          <b-form-group>
            <b-form-input 
              id="login-user"
              v-model="auth.data.username"
              type="text"
              placeholder="Enter username"/>
          </b-form-group>
          <b-form-group>
            <b-form-input 
              id="login-pass"
              v-model="auth.data.password1"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="modal('forgot')"><small>Forgot your password?</small></b-link> | 
          <b-link 
            class="text-danger" 
            @click="modal('signup')"><small>Create an account</small></b-link>
        </div>
        <div v-if="auth.form === 'forgot'">
          <b-form-group>
            <b-form-input 
              id="forgot-email"
              v-model="auth.data.email"
              type="text"
              placeholder="Enter your email"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="modal('login')"><small>I already have an account</small></b-link>
        </div>
        <div v-if="auth.form === 'signup'">
          <p>
            <b-link
              href="https://t.me/CuraNetworkBounty"
              target="_blank"
            >Click here</b-link> to join the bounty Telegram group
          </p>
          <b-form-group>
            <b-form-input 
              id="signup-user"
              v-model="auth.data.username"
              type="text"
              placeholder="Enter Telegram username"/>
          </b-form-group>
          <b-form-group>
            <b-form-input 
              id="signup-email"
              v-model="auth.data.email"
              type="email"
              placeholder="Enter email"/>
          </b-form-group>
          <b-form-group
            description="CAUTION: This cannot be changed. All tokens will be sent to this address during token distribution">
            <b-form-input 
              id="signup-eth-address"
              v-model="auth.data.ethAddress"
              type="text"
              placeholder="Enter Ethereum Address"/>
          </b-form-group>
          <b-form-group
            description="Password">
            <b-form-input 
              id="signup-pass"
              v-model="auth.data.password1"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-form-group
            description="Retype password">
            <b-form-input 
              id="login-pass"
              v-model="auth.data.password2"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="modal('login')"><small>I already have an account</small></b-link>
        </div>
      </b-form>
    </b-modal>
  </section>
</template>

<script>
export default {
  data: () => ({
    auth: {
      form: 'login',
      title: 'Log in',
      action: 'Log in',
      data: {
        username: '',
        email: '',
        ethAddress: '',
        password1: '',
        password2: ''
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
    },

    handleAuthForm(evt) {
      alert(evt)
    }
  }
}
</script>

<style>
</style>
