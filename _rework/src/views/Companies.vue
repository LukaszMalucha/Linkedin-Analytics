<template>
<div class="row plain-element">
  <div class="row header">
          <div class="col-xs-1 col-sm-1 col-md-1 col-lg-1 text-left plain-element">
              <img src="@/assets/finance-medium.jpg" class="img responsive img-header">
          </div>
          <div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 plain-element">
              <div class="row summary">
                   <div class="box">
                      <h5>Financial Companies Listing </h5>
                  </div>
                  <h6>Sector Companies: <b class="counter">{{companiesCount}}</b></h6>
              </div>
          </div>

  </div>
  <div class="dashboard-cards">
      <div class="row row-cards">
          <div class="col-md-4">
            <div v-for="(company, i) in results" class="card company-card" :key="i">
                <div class="card-header">
                   <div class="row plain-element">
                        <div class="col-md-4 plain-element">
                            <div class="card-image">
                                <img src="https://media.licdn.com/dms/image/C4D0BAQE0TbRCFIFQbw/company-logo_200_200/0?e=2132524800&v=beta&t=0ry7PEttBxSu7IOgU9vIT87xU3nTHlPmlm1e5kMpiHw"
                                     class="img responsive">
                            </div>
                            </div>
                        <div class="col-md-8 plain-element">
                        <div class="card-title text-left">
                            <h5>123.ie</h5>
                            <table class="table table-company">
                                <tbody>
                                <tr>
                                    <td>Co. Type:</td>
                                    <td><b>Privately Held</b></td>
                                </tr>
                                <tr>
                                    <td>Industry:</td>
                                    <td><b>Insurance</b></td>
                                </tr>
                                <tr>
                                    <td>Employees:</td>
                                    <td><b>201-500</b></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                       </div>
                </div>
                </div>
                <div class="card-content">
                    <p>Company established in 2002. 123.ie specializes in: Not Specified</p>
                    <br>
                    <td>Website:  </td>
                    <td><b class="company_website">www.123.ie</b></td>
                </div>

            </div>
        </div>
      </div>
  </div>
</div>
</template>


<script>
import { apiService } from "@/common/api.service.js";


export default {
  name: "Companies",
  components: {

  },
  data() {
    return{
      results: {},
      companiesCount: 0
    }
  },
  methods: {
    getCompaniesData() {
    let endpoint = "/api/finance-list/";
    apiService(endpoint)
      .then(data => {
          this.results = data.results,
          this.companiesCount = data.count
          window.console.log(data.results)
      })
      }
  },
  created() {
    this.getCompaniesData();
    window.console.log(this.results)
  }
}

</script>