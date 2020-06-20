using Microsoft.EntityFrameworkCore;

namespace CoronaStat.Models
{
	public class CovidLocationDbContext : DbContext
	{
		public CovidLocationDbContext(DbContextOptions options) : base(options)
		{}
		public DbSet<LocationData> LocationDataStorage { get; set; }
	}
}
