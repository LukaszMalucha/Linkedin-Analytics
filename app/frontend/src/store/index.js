import Vuex from 'vuex';
import Vue from 'vue';
import companies from './modules/companies';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    companies
  }
});