# -*- coding: utf-8 -*-

# Copyright (C) 2010 - 2012, A. Murat Eren
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.

pretty_names = {'output_directory': 'Output directory',
                'project': 'Project',
                'run_date': 'Run date',
                'version': 'Library version',
                'cmd_line': 'Command line',
                'info_file_path': 'Extraction info output file',
                'alignment': 'Input alignment',
                'entropy': 'Input entropy file',
                'total_seq': 'Number of sequences analyzed',
                'alignment_length': 'Number of characters in each alignment',
                'number_of_auto_components': 'Number of entropy components to be selected automatically',
                'number_of_selected_components': 'Number of entropy components chosen by the user',
                'num_reads_eliminated_due_to_min_base_quality': 'Number of reads eliminated due to --min-base-quality',
                'num_oligos_after_l_elim': 'Number of oligotypes left after --limit-oligotypes-to elimination',
                's': 'Min number of datasets oligotype expected to appear',
                'a': 'Min % abundance of oligotype in at least one dataset',
                'A': 'Min total abundance of oligotype in all datasets',
                'T': 'Cosine similarty threshold for oligotype partitioning',
                'q': 'Min PHRED score for each base of interes in every read',
                'quals_provided': 'Quality scores were provided',
                'blast_ref_db_provided': 'Reference DB were provided for local BLAST search',
                'blast_ref_db': 'Reference DB for local BLAST search',
                'limit_oligotypes_to': 'Discard all other oligotypes except',
                'bases_of_interest_locs': 'Base locations of interest in the alignment',
                'num_datasets_in_fasta': 'Number of datasets found',
                'num_unique_oligos': 'Number of unique oligotypes (raw)',
                'num_oligos_after_s_elim': 'Oligotypes after "min number of datasets" elimination',
                'num_oligos_after_a_elim': 'Oligotypes after "min % abundance in a dataset" elimination',
                'num_oligos_after_A_elim': 'Oligotypes after "min total abundance (-A)" elimination',
                'num_sequences_after_qc': 'Number of sequences represented after quality filtering',
                'datasets_removed_after_qc': 'Datasets removed for having 0 oligotypes left after filtering',
                'oligos_fasta_file_path': 'FASTA file for abundant oligotypes',
                'representative_seqs_fasta_file_path': 'Representative sequences per oligotype',
                'oligos_nexus_file_path': 'NEXUS file for abundant oligotypes',
                'environment_file_path': 'Environment file for Viamics/UniFrac analysis',
                'matrix_count_file_path': 'Sample/oligotype abundance data matrix (counts)',
                'matrix_percent_file_path': 'Sample/oligotype abundance data matrix (percents)',
                'oligos_across_datasets_MN_file_path': 'Oligotypes across datasets matrix (MAX normalized)',
                'oligos_across_datasets_SN_file_path': 'Oligotypes across datasets matrix (SUM normalized)',
                'oligotype_partitions_file_path': 'Serialized list of lists for partitioned oligotypes',
                'oligotype_partitions_info': 'Partitioning oligotypes based on frequency patterns',
                'viamics_datasets_dict_file_path': 'Serialized Viamics datasets dictionary',
                'output_directory_for_reps': 'Representative sequences for oligotypes directory',
                'random_color_file_path': 'Random colors for oligotypes',
                'stack_bar_file_path': 'Oligotype distribution stack bar figure',
                'output_directory_for_datasets': 'Directory to store datasets associted information'}