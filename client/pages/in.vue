<template>
  <section class="container mt-5">
    <b-container>
      <b-row>
        <b-col>
          <p>Email:
            <b-form-input
              :value="$auth.user.email"
              type="text"
              disabled/></p>
          <p>Ethereum address:    
            <b-form-input
              :value="$auth.user.eth_address"
              type="text"
              disabled/>
          </p>
        </b-col>
        <b-col class="text-right">
          <p><span class="display-1 text-danger">{{ $auth.user.total_stakes }}</span><br><span>stakes won</span></p>
        </b-col>
      </b-row>
    </b-container>
    <div class="mt-3">
      <b-btn 
        :to="{ name: 'index' }"
        class="float-right" 
        variant="primary">View all bounties</b-btn>
      <b-tabs 
        class="mt-3"
        variant="danger"
        pills
        card>
        <b-tab active>
          <template slot="title">
            Active Hunts
            <b-badge 
              pill 
              variant="light">5</b-badge>
          </template>
          <b-card-group 
            columns
            class="mb-3">
            <b-card
              text-variant="dark"
              header-bg-variant="primary"
              header-text-variant="white">
              <template slot="header">
                Facebook
                <span class="float-right badge pill badge-light text-primary">23 stakes</span>
              </template>
              <p class="card-text">Like, share, and post about Cura Network on Facebook.</p>
              <b-button-group>
                <b-button 
                  href="#"
                  variant="outline-primary">Details</b-button>
                <b-button 
                  v-b-modal.report
                  href="#"
                  variant="outline-primary"
                  @click="report.title = 'Facebook'">Submit report</b-button>
              </b-button-group>
            </b-card>
            <b-card
              text-variant="dark"
              header="Bitcointalk Signature"
              header-bg-variant="secondary"
              header-text-variant="white"
              class="text-center">
              <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <b-button-group>
                <b-button 
                  href="#"
                  variant="outline-secondary">Details</b-button>
                <b-button 
                  href="#"
                  variant="outline-secondary">Submit report</b-button>
              </b-button-group>
            </b-card>
            <b-card 
              text-variant="dark"
              header="Article/Content"
              header-bg-variant="success"
              header-text-variant="white"
              class="text-center">
              <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <b-button-group>
                <b-button 
                  href="#"
                  variant="outline-success">Details</b-button>
                <b-button 
                  href="#"
                  variant="outline-success">Submit report</b-button>
              </b-button-group>
            </b-card>
          </b-card-group>
          <b-card-group 
            columns
            class="mb-3">
            <b-card 
              text-variant="dark"
              header="Twitter"
              header-bg-variant="info"
              header-text-variant="white"
              class="text-center">
              <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <b-button-group>
                <b-button 
                  href="#"
                  variant="outline-info">Details</b-button>
                <b-button 
                  href="#"
                  variant="outline-info">Submit report</b-button>
              </b-button-group>
            </b-card>
            <b-card
              text-variant="dark"
              header="Translation"
              header-bg-variant="warning"
              header-text-variant="dark"
              class="text-center">
              <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              <b-button-group>
                <b-button 
                  href="#"
                  variant="outline-warning">Details</b-button>
                <b-button 
                  href="#"
                  variant="outline-warning">Submit report</b-button>
              </b-button-group>
            </b-card>
          </b-card-group>
        </b-tab>
        <b-tab>
          <template slot="title">
            Reports
            <b-badge 
              pill 
              variant="light">3</b-badge>
          </template>
          <b-table 
            :items="reports" 
            :fields="fields" 
            striped 
            hover/>
        </b-tab>
      </b-tabs>
    </div>
    <b-modal 
      id="report" 
      :title="report.title" 
      ok-title="Submit"
      centered
      ok-variant="danger"
      ok-only
      @ok="console.log('hello')">
      <b-form>
        <p><b-link href="https://facebook.com/curanetwork">Click here</b-link> to like our Facebook page</p>
        <b-form-input 
          id="report-fb-profile"
          type="text"
          placeholder="Facebook profile link"/>
      </b-form>
    </b-modal>
  </section>
</template>

<script>
export default {
  middleware: 'auth',
  data: () => ({
    report: {
      title: 'Facebook',
      fields: []
    },
    fields: ['bounty', 'details', 'date', 'status'],
    reports: [
      {
        bounty: 'Facebook',
        details: 'URL: https://fb.com/posts/3e242424',
        date: '24-04-2018 06:24:02PM',
        status: 'approved'
      },
      {
        bounty: 'Facebook',
        details: 'URL: https://fb.com/posts/3e242424',
        date: '24-04-2018 06:24:02PM',
        status: 'approved'
      },
      {
        bounty: 'Facebook',
        details: 'URL: https://fb.com/posts/3e242424',
        date: '24-04-2018 06:24:02PM',
        status: 'approved'
      }
    ]
  })
}
</script>

<style>
</style>
