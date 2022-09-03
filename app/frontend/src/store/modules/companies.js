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
  followersCountData: {},
  employeeCountData : {},
  companyTypesData : {},
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
  getFollowersCountData: state => state.followersCountData,
  getEmployeeCountData: state => state.employeeCountData,
  getCompanyTypesData: state => state.companyTypesData,
};



const actions = {
  async fetchCompanies({ commit }, category) {
   const response = await api.getCompaniesData(category);

   commit("setCompanies", response.results);
  },
  async fetchSectorData({ commit, dispatch }, category) {
   const response = await api.getSectorData(category);
   commit("setCompanyCount", response.count);
   commit("setCompanyCategory", response.sector_strings[0]);
   commit("setOldestTenCompanies", response.oldest_10_dict);
   commit("setSpecialties", response.spec_dict);
   commit("setFollowersCount", response.followers_dict);
   commit("setEmployeeCount", response.e_count_dict);
   commit("setCompanyTypes", response.type_dict);
   dispatch ("fillFollowersCountChart", response.followers_dict);
   dispatch ("fillEmployeeCountChart", response.e_count_dict);
   dispatch ("fillCompanyTypesChart", response.type_dict);
  },
  fillFollowersCountChart({ commit }, dataset) {
    const dataLabelsFollowers = Object.keys(dataset);
    const dataValuesFollowers = Object.values(dataset);
    const countDataFollowers = {
      labels: dataLabelsFollowers,
      datasets: [
        {
          backgroundColor: ["#4e79a7", "#f28e2b"],
          data: dataValuesFollowers
        }
      ]
    };
    commit("setFollowersCountData", countDataFollowers)
  },
  fillEmployeeCountChart({ commit }, dataset) {
    const dataLabelsEmployees = Object.keys(dataset);
    const dataValuesEmployees = Object.values(dataset);
    const countDataEmployees = {
        labels: dataLabelsEmployees,
        datasets: [
          {
            backgroundColor: ["#2b5b89","#356899", "#5789b6", "#7bb0d5", "#89bddc", "#90c3df", "#98c8e2", "#9ccae3", "#9ccae3"],
            data: dataValuesEmployees
          }
        ]
    };
    commit("setEmployeeCountData", countDataEmployees)
  },
  fillCompanyTypesChart({ commit }, dataset) {
    const dataLabelsCompanyTypes = Object.keys(dataset);
    const dataValuesCompanyTypes = Object.values(dataset);
    const countDataCompanyTypes = {
        labels: dataLabelsCompanyTypes,
        datasets: [
          {
            backgroundColor: ["#4e79a7","#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc948"],
            data: dataValuesCompanyTypes
          }
        ]
    };
    commit("setCompanyTypesData", countDataCompanyTypes)
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
  setFollowersCountData: (state, followersCountData) => {
    state.followersCountData = followersCountData
  },
  setEmployeeCountData: (state, employeeCountData) => {
    state.employeeCountData = employeeCountData
  },
  setCompanyTypesData: (state, companyTypesData) => {
    state.companyTypesData = companyTypesData
  },
}

export default {
  state,
  getters,
  actions,
  mutations
}













