import { apiService } from "@/common/api.service.js";

export default {
  getCompaniesData(category) {
    let endpoint = `/api/${category}-list/`;
    return apiService(endpoint)
  },
  getSectorData(category) {
    let endpoint = `/api/${category}/`;
    return apiService(endpoint);
  }
}