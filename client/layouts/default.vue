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
            v-if="!$auth.loggedIn"
            href="#">Log in</b-nav-item>
          <b-nav-item 
            v-if="$auth.loggedIn"
            :to="{ name: 'in'
          }">@jeffjenkins</b-nav-item>

          <b-nav-item 
            v-if="$auth.loggedIn" 
            href="#" 
            @click="$auth.logout">Log out</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <nuxt/>

  </div>
</template>

<script>
export default {
  data: () => ({}),
  methods: {}
}
</script>
