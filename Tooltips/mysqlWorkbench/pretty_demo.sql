USE kickstarter;
select name, pledged, backers from campaign where pledged/backers is not null and outcome != 'failed';