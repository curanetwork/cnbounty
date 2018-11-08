<template>
  <div>
    <b-navbar 
      toggleable="md" 
      type="dark" 
      variant="danger">

      <b-navbar-toggle target="nav_collapse"/>

      <b-navbar-brand href="https://curanetwork.co">Cura Network Bounty</b-navbar-brand>

      <b-collapse 
        id="nav_collapse" 
        is-nav>

        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item 
            href="#" 
            disabled>Disabled</b-nav-item>
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
            v-b-modal.login
            href="#"
            @click="auth = 'login'">Log in</b-nav-item>

          <!-- Modal Component -->
          <b-modal 
            id="login" 
            centered 
            title="Login"
            ok-title="Submit"
            ok-variant="danger"
            ok-only
            @ok="login()">
            <b-form v-if="auth === 'login'">
              <b-form-group
                label="Username:"
                label-for="login-user">
                <b-form-input 
                  id="login-user"
                  type="text"
                  placeholder="Enter username"/>
              </b-form-group>
              <b-form-group 
                label="Password"
                label-for="login-pass">
                <b-form-input 
                  id="login-pass"
                  type="password"
                  placeholder="**********"/>
              </b-form-group>
            </b-form>
          </b-modal>

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <nuxt/>
  </div>
</template>

<script>
export default {
  data: () => ({
    auth: ''
  }),
  methods: {
    login() {
      alert('hello world!')
    }
  }
}
</script>
