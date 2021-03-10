<template>
    <div id="app">
        <h1 class="title-text">Charfinder</h1>
        <Examples/>
        <CharForm
            @ask-char="askChar"
        />
        <MyScrollLoader
            :loadMore="loadMore"
            :page="page"
            :pageSize="pageSize"
            :chars="chars"
            :query="query"
        />
        <div id="copyright-container">
          <a class="copyright-container__link" href="https://github.com/osipov-andrey">
            <p class="copyright-container__text">By osipov-andrey</p>
          </a>
        </div>
    </div>


</template>

<script>

    import CharForm from '@/components/CharForm'
    import Examples from '@/components/Examples'
    import MyScrollLoader from '@/components/MyScrollLoader'

export default {
        data() {
          return {
            loadMore: false,
            page: 1,
            pageSize: 40,
            chars: [],
            query: '',
          }
        },
    components: {
        CharForm,
        Examples,
        MyScrollLoader
    },
        methods: {
            askChar(char){
                this.query = char
                this.chars = []
                this.loadMore = true
                this.page = 1
            }
        },
        created() {
            console.log(this.viewport)
            // if query in query-params - call getCharsInfo
            // This works with examples
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            let query = params.get("query")
            if (query) {
                this.query = query
                this.loadMore = true
                // this.getCharsInfo()
            }
        }
      }
</script>

