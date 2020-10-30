<template>
<div class="row plain-element">
  <MessageComponent/>
  <div class="dashboard-cards">
      <div class="row header transparent header-small">

      </div>
      <div class="row row-cards">
          <div class="col s12 m6 l4">
              <div class="card menu-card">
                  <div class="card-top">
                      <i class="fas fa-chart-bar"></i> Financial Sector
                  </div>
                  <div class="card-header">
                      <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/portrait.png" class="img-responsive">
                      <p><b>Lukasz Malucha</b> <br>Python Developer</p>
                      <a target="_blank" href="https://www.linkedin.com/in/lukaszmalucha/">
                        <div class="dots">
                            &#9642;
                            &#9642;
                            &#9642;
                        </div>
                      </a>
                  </div>
                  <div class="card-content">
                      <div class="row row-comment">
                          Visualizing <b>Financial Companies</b> located in Ireland
                      </div>

                      <div class="row row-image">
                          <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/finance.jpg" class="img-responsive img-card">
                      </div>
                      <router-link :to="{ name: 'sector', params: { category: 'finance' } }">
                        <button class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
                      </router-link>
                  </div>
                  <div class="card-bottom">
                  </div>
              </div>
          </div>
          <div class="col s12 m6 l4">
              <div class="card menu-card">
                  <div class="card-top">
                      <i class="fa fa-laptop"></i> IT Sector
                  </div>
                  <div class="card-header">
                      <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/portrait.png" class="img-responsive">
                      <p><b>Lukasz Malucha</b> <br>Python Developer</p>
                      <a target="_blank" href="https://www.linkedin.com/in/lukaszmalucha/">
                      <div class="dots">
                          &#9642;
                          &#9642;
                          &#9642;
                      </div>
                      </a>
                  </div>
                  <div class="card-content">
                      <div class="row row-comment">
                          Visualizing <b>IT Companies</b> located in Ireland
                      </div>

                      <div class="row row-image">
                          <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/it.jpg" class="img-responsive img-card">
                      </div>
                      <router-link :to="{ name: 'sector', params: { category: 'it' } }">
                        <button class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
                      </router-link>
                  </div>
                  <div class="card-bottom">
                  </div>
              </div>
          </div>
          <div class="col s12 m6 l4">
              <div class="card menu-card">
                  <div class="card-top">
                      <i class="fa fa-graduation-cap"></i> Educational Institutions
                  </div>
                  <div class="card-header">

                      <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/portrait.png" class="img-responsive">
                      <p><b>Lukasz Malucha</b> <br>Python Developer</p>
                      <a target="_blank" href="https://www.linkedin.com/in/lukaszmalucha/">
                      <div class="dots">
                          &#9642;
                          &#9642;
                          &#9642;
                      </div>
                      </a>
                  </div>
                  <div class="card-content">
                      <div class="row row-comment">
                          Visualizing <b>Educational Institutions</b> located in Ireland
                      </div>

                      <div class="row row-image">
                          <img src="https://linkedin-analytics.s3.amazonaws.com/static/img/college.jpg" class="img-responsive img-card">
                      </div>
                      <router-link :to="{ name: 'sector', params: { category: 'education' } }">
                        <button class="btn btn-enter"><span>Continue <i class="far fa-arrow-alt-circle-right"></i></span></button>
                      </router-link>
                  </div>
                  <div class="card-bottom">
                  </div>
              </div>
          </div>
      </div>
  </div>
</div>
</template>

<script>
import MessageComponent from "@/components/MessageComponent.vue";

export default {
  name: 'home',
  components: {
    MessageComponent
  },
  created() {
    document.title = "Linkedin Analytics - Irish companies insights | Septellar";
  }
};

</script>
