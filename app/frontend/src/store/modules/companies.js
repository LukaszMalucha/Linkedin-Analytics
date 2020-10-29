import api from "../../api/api.js";


const state = {
  companies: [],
  error: null,
  message: null,
}

const getters = {
  getCompanies: state => state.companies,
  getError: state => state.error,
  getMessage: state => state.message
};


const actions = {
  async fetchCompanies({ commit }, category) {
   const response = await api.getCompaniesData(category);
   window.console.log(response);
   commit("setCompanies", response);

  }
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
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}













