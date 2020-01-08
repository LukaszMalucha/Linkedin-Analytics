<template>
<div class="row plain-element">
  <div class="row header">
      <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 text-left plain-element">
          <img src="https://linkedin-analytics.s3-eu-west-1.amazonaws.com/static/img/insights/404.jpg" class="img responsive img-header">
      </div>
      <div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 plain-element">
          <div class="row summary">
               <div class="box">
                  <h5> 404 - Page Not Found </h5>
                  <router-link class="btn-algorithm" :to="{ name: 'home' }">
                    Back to Dashboard
                  </router-link>
              </div>
          </div>
      </div>
  </div>
</div>
</template>


<script>


export default {
  name: "NotFound",
  components: {
  },
  data() {
    return {
      message: "404 - Page Not Found"
    }
  }
}
</script>