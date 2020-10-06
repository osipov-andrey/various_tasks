<template>
    <div id="app">
        <h1 class="title-text">Charfinder</h1>
        <Examples/>
        <CharForm
            @ask-char="askChar"
        />
        <div class="images-container">
          <div v-for="(char, index) of chars" :key="index">
            <div class="images-card">
                <p :char="char">{{char.code_str}} <b>{{char.char}}</b> {{char.name}}</p>
            </div>
          </div>
        </div>

        <scroll-loader
                :loader-method="getCharsInfo"
                :loader-enable="loadMore"
                :loader-disable="!loadMore"
        ></scroll-loader>

        <div class="copyright-container">
          <a class="copyright-container__link" href="https://github.com/osipov-andrey">
            <p class="copyright-container__text">By osipov-andrey</p>
          </a>
        </div>
    </div>


</template>

<script>
    import axios from 'axios';

    import Vue from 'vue'
    import ScrollLoader from 'vue-scroll-loader'
    import CharForm from '@/components/CharForm'
    import Examples from '@/components/Examples'

    Vue.use(ScrollLoader)

export default {
        data() {
          return {
            loadMore: false,
            page: 1,
            pageSize: 20,
            chars: [],
              masks: [],
              query: ''
          }
        },
    components: {
        CharForm,
        Examples
    },
        methods: {
          getCharsInfo() {
            axios.get('http://127.0.0.1:8888', {
                params: {
                  page: this.page++,
                  per_page: this.pageSize,
                    query: this.query
                }
              })
              .then(res => {
                  console.log(res.data)
                  res.data && (this.chars = [...this.chars, ...res.data])
                  // this.images.push(res.data)
                  console.log(this.chars)

                // Stop scroll-loader
                res.data.length < this.pageSize && (this.loadMore = false)
              })
              .catch(error => {
                console.log(error);
              })
          },
            askChar(char){
                this.query = char
                this.chars = []
                this.loadMore = true
                this.page = 1
            }
        },
        created() {
            // if query in query-params - call getCharsInfo
            // This works with examples
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            let query = params.get("query")
            if (query) {
                this.query = query
                this.getCharsInfo()
            }
        }
      }
</script>

