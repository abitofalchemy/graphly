/* -*- mode: C -*-  */
/* vim:set ts=2 sw=2 sts=2 et: */
/*
 IGraph library.
 Copyright (C) 2011-2012  Gabor Csardi <csardi.gabor@gmail.com>
 334 Harvard street, Cambridge, MA 02139 USA
 
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc.,  51 Franklin Street, Fifth Floor, Boston, MA
 02110-1301 USA
 
 */

#include <igraph.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

/* Links:
 * http://stackoverflow.com/questions/10225603/print-igraph-vector-ptr-tlist-of-vectors-igraph-vector-t
 */

void gsumary(const igraph_t * g){
    printf("|V|=%d |E|=%d directed=%d\n", (int)igraph_vcount(g), (int)igraph_ecount(g), (int)igraph_is_directed(g));
}

void show_results(igraph_vector_t * membership, igraph_real_t codelength) {
    printf("Codelength: %0.5f (in %d modules)\n", codelength, (int)igraph_vector_max(membership) + 1 );
    printf("Membership: ");
    int i;
    for (i=0; i < igraph_vector_size(membership); i++) {
        printf("%li ", (long)VECTOR(*membership)[i] );
    }
    printf("\n");
}

void show_results_lite(igraph_vector_t * membership, igraph_real_t codelength) {
    printf("Codelength: %0.5f (in %d modules)\n", codelength, (int)igraph_vector_max(membership) + 1 );
    printf("Membership (1/100 of vertices): ");
    int i;
    for (i=0; i < igraph_vector_size(membership); i+=100) {
        printf("%li ", (long)VECTOR(*membership)[i] );
    }
    printf("\n");
}

void infomap_weighted_test(const igraph_t * g, const igraph_vector_t *weights){
    igraph_vector_t membership;
    igraph_real_t codelength = 1000;
    igraph_vector_init(&membership, 0);
    
    igraph_community_infomap(/*in */ g, /*e_weight=*/ weights, NULL, /*nb_trials=*/5,
                             /*out*/ &membership, &codelength);
    if(igraph_vcount(g) > 500)
        show_results_lite(&membership, codelength);
    else
        show_results(&membership, codelength);
    
    igraph_vector_destroy(&membership);
}



void infomap_test(const igraph_t * g){
    infomap_weighted_test(g, 0);
}
/*  gcc igraph_test.c -I /usr/local/include/igraph -L /usr/local/lib -ligraph -o igraph_tst
 */
int main() {
    igraph_t g;
    igraph_vector_t v;
    //igraph_vector_t weights;
    /* Two triangles connected by one edge */
    printf("# Read a wikipedia edgelist\n");
    
    // Get the $HOME dir 
//    char cwd[1024];
//    if (getcwd(cwd, sizeof(cwd)) != NULL)
//       fprintf(stdout, "Current working dir: %s\n", cwd);
//    else
//       perror("getcwd() error");
    char *homedir = getenv("HOME");
    
    if (homedir != NULL)    printf("Home dir in enviroment: %s\n\n", homedir);
    else                    perror("getenv('HOME') error");
    char *el_file_path = "/data/saguinag/datasets/enwiki/toypage.txt";
    if (homedir != NULL)    printf("File path: \n%s\n", el_file_path);
    else                    perror("getenv('HOME') error");
    
    FILE *wikt = fopen( "/data/saguinag/datasets/enwiki/toypage.txt", "r");
    igraph_read_graph_edgelist(&g, wikt,0,0);
    fclose(wikt);
    
    gsumary(&g);        // graph summary
    

    // Get the vector of nodes
    //          igraph_bool_t *res))

    
    // infomap_test(&g);   
    igraph_destroy(&g);
    
    exit(0);
}
