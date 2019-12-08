<template>
<div id="page-index">
  <div class="row row-banner row-banner-small">
    <div class="col-md-8 text-left col-banner-small no-padding">
      <h4>{{ message }}</h4>
    </div>
    <div class="col-md-4 no-padding">
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