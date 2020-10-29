import { apiService } from "@/common/api.service.js";

export default {
  getCompaniesData(category) {
    let endpoint = `/api/${category}-list/`;
    window.console.log(endpoint)
    return apiService(endpoint)
  }
}