<template>
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
    }
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
