<template>
<div class="row plain-element">
  <div class="row header">
      <div class="row">
          <div class="col-xs-2 col-sm-2 col-md-1 col-lg-2 text-right">
              <img src="@/assets/finance-medium.jpg" class="img responsive img-header">
          </div>

          <div class="col-xs-10 col-sm-10 col-md-11 col-lg-10">
              <div class="row summary">
                   <div class="box">
                      <h5>Financial Companies in Ireland </h5>
                      <a href="" class="btn-algorithm">View Companies</a>
                  </div>

                  <h6>Sector Companies: <b class="counter">12</b></h6>


              </div>
          </div>
      </div>
  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-md-3 no-padding">
              <div class="row no-padding no-margin-bottom">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>Financial Companies </p>

                      </div>
                      <div class="row row-comment">
                          Financial Companies with the tradition:
                      </div>

                      <div class="row-image">
                          <div class="table-responsive">
                              <table class="table table-established">
                                  <thead>
                                  <tr>
                                      <th>Company</th>
                                      <th class="center">Established</th>
                                  </tr>
                                  </thead>
                                  <tbody>

                                  <tr>
                                      <td>IT search</td>
                                      <td class="center">1899</td>
                                  </tr>

                                  </tbody>
                              </table>
                          </div>
                      </div>
                  </div>
              </div>
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>Financial Companies </p>
                      </div>
                      <div class="row row-comment">
                          Financial Companies by followers count:
                      </div>
                      <div class="chart-small">
                          <canvas id="followersChart"></canvas>
                      </div>
                  </div>
              </div>
          </div>

          <div class="col-md-6 no-padding">
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>Financial Companies </p>

                      </div>
                      <div class="row row-comment">
                          Financial Companies by type:
                      </div>
                      <div class="chart">
                          <canvas id="typeChart"></canvas>
                      </div>
                  </div>
              </div>
              <div class="row no-padding">
                  <div class="card insights-card">
                      <div class="card-header">
                          <img src="@/assets/finance-small.jpg" class="img-responsive">
                          <p><b>Linkedin Analytics</b> <br>Financial Companies </p>

                      </div>
                      <div class="row row-comment">
                          Financial Companies by employee count:
                      </div>
                      <div class="chart">
                          <canvas id="ecountChart"></canvas>
                      </div>
                  </div>
              </div>
          </div>
          <div class="col-md-3 no-padding">
              <div class="card insights-card">
                  <div class="card-header">
                      <img src="@/assets/finance-small.jpg" class="img-responsive">
                      <p><b>Linkedin Analytics</b> <br>Financial Companies</p>
                  </div>
                  <div class="row row-comment">
                      Financial Companies business specialties:
                  </div>
                  <div class="row-image">
                      <div class="table-responsive">
                          <table class="table table-established table-long">
                              <thead>
                              <tr>
                                  <th>Specialty</th>
                                  <th class="center">Occurence</th>
                              </tr>
                              </thead>
                              <tbody>

                              <tr>
                                  <td>IT</td>
                                  <td class="center">12</td>
                              </tr>

                              </tbody>
                          </table>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</div>
</template>


<script>

export default {
  name: 'finance',
  components: {

  },
  created() {
    document.title = "Linkedin Analytics - Financial Companies";
  }
};

</script>
