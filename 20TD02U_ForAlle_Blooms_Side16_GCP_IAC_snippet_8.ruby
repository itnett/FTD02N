describe google_compute_instance(project: 'my-project', zone: 'us-central1-a', name: 'my-instance') do
     it { should exist }
     its('machine_type') { should match 'n1-standard-1' }
   end