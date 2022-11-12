# Commands

Track Job Applications support basic commands to add, delete or update the job applications. Apart from it, it also has the ability to generate a basic report which gives some insights on the applications saved.

> Note: By default, all the commands are executed on the entire data. In order to run it on the subset of applications, `--start-date` and `--end-date` can be given in `YYYY-MM-DD` format to perform the operations for application that have the `applied_at` date between this range (inclusive).

All the commands mentioned henceforth have a `--help` flag that can be used to get information about them.

### Basic Commands

#### -v/--version

:::track.cli.get_version

#### add

:::track.cli.add

#### ls

:::track.cli.ls

#### rm

:::track.cli.rm

### Update Commands

#### update company

:::track.update_cli.company

#### update position

:::track.update_cli.position

#### update status

:::track.update_cli.status

#### update applied_at

:::track.update_cli.applied_at

### Report Commands

#### report

:::track.report_cli.default

#### counts

:::track.report_cli.counts

#### status

:::track.report_cli.status

#### shortlisted

:::track.report_cli.shortlisted
