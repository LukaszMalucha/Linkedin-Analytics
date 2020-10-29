<template>
<div class="plain-element">
  <div  id="alert" class="alert alert-danger" role="alert">
    {{ getError() }}
  </div>
  <div  id="alertSuccess" class="alert alert-success" role="alert">
    {{ getMessage() }}
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: "MessageComponent",
  methods: {
  ...mapGetters(['getError', 'getMessage']),
  }
};

</script>

