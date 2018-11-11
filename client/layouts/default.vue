<template>
  <div>
    <b-navbar 
      toggleable="md" 
      type="dark" 
      variant="danger">

      <b-navbar-toggle target="nav_collapse"/>

      <b-navbar-brand href="/">
        <img 
          src="/logo.png" 
          class="d-inline-block align-top" 
          width="auto"
          height="30px"
          alt="Cura Network">
        Cura Network Bounty
      </b-navbar-brand>

      <b-collapse 
        id="nav_collapse" 
        is-nav>

        <b-navbar-nav>
          <b-nav-item 
            :to="{ name: 'index'
          }">All Bounties</b-nav-item>
          <b-nav-item href="https://t.me/CuraNetworkBounty">Telegram</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-form>
            <b-form-input 
              size="sm" 
              class="mr-sm-2" 
              type="text" 
              placeholder="Search"/>
            <b-button 
              size="sm" 
              class="my-2 my-sm-0" 
              type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item 
            v-b-modal.auth
            href="#"
            @click="auth = {
              form: 'login',
              title: 'Log in',
              action: 'Log in' 
          }">Log in</b-nav-item>
          <b-nav-item 
            :to="{ name: 'in'
          }">@jeffjenkins</b-nav-item>

          <b-nav-item href="#">Log out</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <nuxt/>

    <!-- Modal Component -->
    <b-modal 
      id="auth" 
      :title="auth.title" 
      :ok-title="auth.action"
      centered
      ok-variant="danger"
      ok-only
      @ok="login()">
      <b-form>
        <div v-if="auth.form === 'login'">
          <b-form-group>
            <b-form-input 
              id="login-user"
              type="text"
              placeholder="Enter username"/>
          </b-form-group>
          <b-form-group>
            <b-form-input 
              id="login-pass"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="auth = {
              form: 'forgot',
              title: 'Reset password',
              action: 'Send me password reset link' 
          }"><small>Forgot your password?</small></b-link> | 
          <b-link 
            class="text-danger" 
            @click="auth = {
              form: 'signup',
              title: 'Create an account',
              action: 'Submit' 
          }"><small>Create an account</small></b-link>
        </div>
        <div v-if="auth.form === 'forgot'">
          <b-form-group>
            <b-form-input 
              id="forgot-email"
              type="text"
              placeholder="Enter your email"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="auth = {
              form: 'login',
              title: 'Log in',
              action: 'Log in' 
          }"><small>I already have an account</small></b-link>
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
              type="text"
              placeholder="Enter Telegram username"/>
          </b-form-group>
          <b-form-group>
            <b-form-input 
              id="signup-email"
              type="email"
              placeholder="Enter email"/>
          </b-form-group>
          <b-form-group
            description="CAUTION: This cannot be changed. All tokens will be sent to this address during token distribution">
            <b-form-input 
              id="signup-eth-address"
              type="text"
              placeholder="Enter Ethereum Address"/>
          </b-form-group>
          <b-form-group
            description="Password">
            <b-form-input 
              id="signup-pass"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-form-group
            description="Retype password">
            <b-form-input 
              id="login-pass"
              type="password"
              placeholder="**********"/>
          </b-form-group>
          <b-link 
            class="text-danger" 
            @click="auth = {
              form: 'login',
              title: 'Log in',
              action: 'Log in' 
          }"><small>I already have an account</small></b-link>
        </div>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
export default {
  data: () => ({
    auth: {
      form: 'login',
      title: 'Log in',
      action: 'Log in'
    }
  }),
  methods: {
    login() {
      alert('hello world!')
    }
  }
}
</script>
