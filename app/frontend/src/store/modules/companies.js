import api from "../../api/api.js";


const state = {
  companies: [],
  error: null,
  message: null,
  title: null,
  companyCount: null,
  companyCategory: null,
  oldestTenCompanies: [],
  specialties: {},
  followersCount: {},
  employeeCount: {},
  companyTypes: {},

}

const getters = {
  getCompanies: state => state.companies,
  getError: state => state.error,
  getMessage: state => state.message,
  getTitle: state => state.title,
  getCompanyCount: state => state.companyCount,
  getCompanyCategory: state => state.companyCategory,
  getOldestTenCompanies: state => state.oldestTenCompanies,
  getSpecialties: state => state.specialties,
  getFollowersCount: state => state.followersCount,
  getEmployeeCount: state => state.employeeCount,
  getCompanyTypes: state => state.companyTypes,
};



const actions = {
  async fetchCompanies({ commit }, category) {
   const response = await api.getCompaniesData(category);

   commit("setCompanies", response.results);
  },
  async fetchSectorData({ commit }) {
   const response = await api.getSectorData("finance");
   window.console.log(response);
   commit("setCompanyCount", response.results.count);
   commit("setCompanyCategory", response.results.sector_strings[0]);
   commit("setOldestTenCompanies", response.results.oldest_10_dict);
   commit("setSpecialties", response.results.spec_dict);
   commit("setFollowersCount", response.results.followers_dict);
   commit("setEmployeeCount", response.results.e_count_dict);
   commit("setCompanyTypes", response.results.type_dict);
  },
  fetchTitle({ commit }, category) {
      if (category == "finance") {
          commit("setTitle", "Financial Companies");
      }
      else if (category == "it") {
          commit("setTitle", "IT Companies");
      }
      else {
          commit("setTitle", "Educational Institutions");
      }
    },
}


const mutations = {
  setCompanies: (state, companies) => {
    state.companies = companies;
  },
  setError: (state, error) => {
    state.error = error;
  },
  setMessage: (state, message) => {
    state.message = message;
  },
  setTitle: (state, title) => {
    state.title = title
  },
  setCompanyCount: (state, companyCount) => {
    state.companyCount = companyCount
  },
  setCompanyCategory: (state, companyCategory) => {
    state.companyCategory = companyCategory
  },
  setOldestTenCompanies: (state, oldestTenCompanies) => {
    state.oldestTenCompanies = oldestTenCompanies
  },
  setSpecialties: (state, specialties) => {
    state.specialties = specialties
  },
  setFollowersCount: (state, followersCount) => {
    state.followersCount = followersCount
  },
  setEmployeeCount: (state, employeeCount) => {
    state.employeeCount = employeeCount
  },
  setCompanyTypes: (state, companyTypes) => {
    state.companyTypes = companyTypes
  },
}

export default {
  state,
  getters,
  actions,
  mutations
}













