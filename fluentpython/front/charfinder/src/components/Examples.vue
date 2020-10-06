<template>
    <div>
        <table>
            <p>Examples:</p>
            <td v-for="(example, index) of examples" :key="index">
                <tr><a :href="example.href">{{example.text}}</a></tr>
            </td>

        </table>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                examples: ''
            }
        },
        created() {
            axios.get('http://127.0.0.1:8888/examples')
              .then(res => {
                  this.examples = res.data
              })
              .catch(error => {
                console.log(error);
              })
        }
    }
</script>
